import { useState, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Calendar, Trash2, RefreshCw } from 'lucide-react'
import axios from 'axios'

interface HistoryItem {
  id: string
  filename: string
  landmark: string
  confidence: number
  timestamp: string
  image_url?: string
}

export function History() {
  const [history, setHistory] = useState<HistoryItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchHistory()
  }, [])

  const fetchHistory = async () => {
    try {
      setLoading(true)
      const response = await axios.get('http://localhost:8000/api/v1/history')
      setHistory(response.data)
    } catch (err) {
      console.error('Error fetching history:', err)
      setError('Failed to load history. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleDeleteItem = async (id: string) => {
    try {
      await axios.delete(`http://localhost:8000/api/v1/history/${id}`)
      setHistory(history.filter(item => item.id !== id))
    } catch (err) {
      console.error('Error deleting item:', err)
    }
  }

  const formatDate = (timestamp: string) => {
    return new Date(timestamp).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 0.8) return 'bg-green-500'
    if (confidence >= 0.6) return 'bg-yellow-500'
    return 'bg-red-500'
  }

  const getConfidenceText = (confidence: number) => {
    if (confidence >= 0.8) return 'High'
    if (confidence >= 0.6) return 'Medium'
    return 'Low'
  }

  if (loading) {
    return (
      <div className="space-y-8">
        <div className="text-center space-y-4">
          <h1 className="text-4xl font-bold">Prediction History</h1>
          <p className="text-xl text-muted-foreground">
            View your recent image analysis results
          </p>
        </div>
        <div className="flex justify-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="space-y-8">
        <div className="text-center space-y-4">
          <h1 className="text-4xl font-bold">Prediction History</h1>
          <p className="text-xl text-muted-foreground">
            View your recent image analysis results
          </p>
        </div>
        <div className="bg-destructive/10 border border-destructive/20 rounded-lg p-4 text-center">
          <p className="text-destructive">{error}</p>
          <Button onClick={fetchHistory} className="mt-4">
            Try Again
          </Button>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <div className="space-y-4">
          <h1 className="text-4xl font-bold">Prediction History</h1>
          <p className="text-xl text-muted-foreground">
            View your recent image analysis results
          </p>
        </div>
        <Button onClick={fetchHistory} variant="outline" className="flex items-center space-x-2">
          <RefreshCw className="h-4 w-4" />
          <span>Refresh</span>
        </Button>
      </div>

      {history.length === 0 ? (
        <div className="text-center py-12">
          <p className="text-muted-foreground text-lg">No predictions yet.</p>
          <p className="text-muted-foreground">Upload an image to get started!</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {history.map((item) => (
            <Card key={item.id} className="overflow-hidden">
              {item.image_url && (
                <div className="aspect-video overflow-hidden">
                  <img
                    src={item.image_url}
                    alt={item.landmark}
                    className="w-full h-full object-cover"
                  />
                </div>
              )}
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="space-y-2">
                    <CardTitle className="text-lg">{item.landmark}</CardTitle>
                    <p className="text-sm text-muted-foreground">{item.filename}</p>
                  </div>
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => handleDeleteItem(item.id)}
                    className="text-destructive hover:text-destructive"
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
                <div className="flex items-center space-x-2">
                  <Badge 
                    variant="secondary" 
                    className={`${getConfidenceColor(item.confidence)} text-white`}
                  >
                    {getConfidenceText(item.confidence)}
                  </Badge>
                  <span className="text-sm text-muted-foreground">
                    {(item.confidence * 100).toFixed(1)}%
                  </span>
                </div>
              </CardHeader>
              <CardContent>
                <div className="flex items-center space-x-2 text-sm text-muted-foreground">
                  <Calendar className="h-4 w-4" />
                  <span>{formatDate(item.timestamp)}</span>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}
