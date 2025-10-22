import { useState, useEffect } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Play, MapPin, Calendar, ExternalLink } from 'lucide-react'
import axios from 'axios'

interface Monument {
  id: string
  title: string
  image: string
  short_text: string
  audio_preview_url?: string
  year_built?: string
  location?: string
  reference_url?: string
}

export function Explore() {
  const [monuments, setMonuments] = useState<Monument[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [playingAudio, setPlayingAudio] = useState<string | null>(null)

  useEffect(() => {
    fetchMonuments()
  }, [])

  const fetchMonuments = async () => {
    try {
      setLoading(true)
      const response = await axios.get('http://localhost:8000/api/v1/explore')
      setMonuments(response.data)
    } catch (err) {
      console.error('Error fetching monuments:', err)
      setError('Failed to load monuments. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handlePlayAudio = (monumentId: string, audioUrl: string) => {
    if (playingAudio === monumentId) {
      // Stop current audio
      setPlayingAudio(null)
    } else {
      // Play new audio
      const audio = new Audio(audioUrl)
      audio.onended = () => setPlayingAudio(null)
      audio.play()
      setPlayingAudio(monumentId)
    }
  }

  if (loading) {
    return (
      <div className="space-y-8">
        <div className="text-center space-y-4">
          <h1 className="text-4xl font-bold">Explore Historical Monuments</h1>
          <p className="text-xl text-muted-foreground">
            Discover curated historical landmarks from around the world
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
          <h1 className="text-4xl font-bold">Explore Historical Monuments</h1>
          <p className="text-xl text-muted-foreground">
            Discover curated historical landmarks from around the world
          </p>
        </div>
        <div className="bg-destructive/10 border border-destructive/20 rounded-lg p-4 text-center">
          <p className="text-destructive">{error}</p>
          <Button onClick={fetchMonuments} className="mt-4">
            Try Again
          </Button>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-8">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold">Explore Historical Monuments</h1>
        <p className="text-xl text-muted-foreground">
          Discover curated historical landmarks from around the world
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {monuments.map((monument) => (
          <Card key={monument.id} className="overflow-hidden">
            <div className="aspect-video overflow-hidden">
              <img
                src={monument.image}
                alt={monument.title}
                className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
              />
            </div>
            <CardHeader>
              <CardTitle className="text-lg">{monument.title}</CardTitle>
              <div className="flex items-center space-x-4 text-sm text-muted-foreground">
                {monument.year_built && (
                  <div className="flex items-center space-x-1">
                    <Calendar className="h-4 w-4" />
                    <span>{monument.year_built}</span>
                  </div>
                )}
                {monument.location && (
                  <div className="flex items-center space-x-1">
                    <MapPin className="h-4 w-4" />
                    <span>{monument.location}</span>
                  </div>
                )}
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              <CardDescription className="text-sm leading-relaxed">
                {monument.short_text}
              </CardDescription>
              
              <div className="flex items-center justify-between">
                {monument.audio_preview_url && (
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => handlePlayAudio(monument.id, monument.audio_preview_url!)}
                    className="flex items-center space-x-2"
                  >
                    <Play className="h-4 w-4" />
                    <span>
                      {playingAudio === monument.id ? 'Playing...' : 'Preview'}
                    </span>
                  </Button>
                )}
                
                {monument.reference_url && (
                  <Button variant="outline" size="sm" asChild>
                    <a
                      href={monument.reference_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center space-x-2"
                    >
                      <ExternalLink className="h-4 w-4" />
                      <span>Learn More</span>
                    </a>
                  </Button>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {monuments.length === 0 && (
        <div className="text-center py-12">
          <p className="text-muted-foreground">No monuments available at the moment.</p>
        </div>
      )}
    </div>
  )
}
