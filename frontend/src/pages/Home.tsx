import { useState } from 'react'
import { ImageUpload } from '@/components/ImageUpload'
import { ResultCard } from '@/components/ResultCard'
import { Button } from '@/components/ui/button'
import { Loader2, Upload } from 'lucide-react'
import axios from 'axios'

interface PredictionResult {
  landmark: string
  confidence: number
  summary: string
  yearBuilt?: string
  location?: string
  imageUrl?: string
  audioUrl?: string
  referenceUrl?: string
}

export function Home() {
  const [selectedImage, setSelectedImage] = useState<File | null>(null)
  const [isProcessing, setIsProcessing] = useState(false)
  const [result, setResult] = useState<PredictionResult | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleImageSelect = (file: File) => {
    setSelectedImage(file)
    setResult(null)
    setError(null)
  }

  const handleClearImage = () => {
    setSelectedImage(null)
    setResult(null)
    setError(null)
  }

  const handlePredict = async () => {
    if (!selectedImage) return

    setIsProcessing(true)
    setError(null)

    try {
      const formData = new FormData()
      formData.append('image', selectedImage)

      const response = await axios.post('http://localhost:8000/api/v1/identify', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

      setResult(response.data)
    } catch (err) {
      console.error('Prediction error:', err)
      setError('Failed to process image. Please try again.')
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <div className="space-y-8">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold">ChronoScope</h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
          Upload a historical image and discover its story. Our AI will identify landmarks, 
          retrieve historical information, and present it as an interactive timeline.
        </p>
      </div>

      <div className="space-y-6">
        <ImageUpload
          onImageSelect={handleImageSelect}
          selectedImage={selectedImage}
          onClearImage={handleClearImage}
          isProcessing={isProcessing}
        />

        {selectedImage && !result && (
          <div className="flex justify-center">
            <Button
              onClick={handlePredict}
              disabled={isProcessing}
              size="lg"
              className="flex items-center space-x-2"
            >
              {isProcessing ? (
                <>
                  <Loader2 className="h-5 w-5 animate-spin" />
                  <span>Processing...</span>
                </>
              ) : (
                <>
                  <Upload className="h-5 w-5" />
                  <span>Analyze Image</span>
                </>
              )}
            </Button>
          </div>
        )}

        {error && (
          <div className="bg-destructive/10 border border-destructive/20 rounded-lg p-4 text-center">
            <p className="text-destructive">{error}</p>
          </div>
        )}

        {result && (
          <ResultCard
            landmark={result.landmark}
            confidence={result.confidence}
            summary={result.summary}
            yearBuilt={result.yearBuilt}
            location={result.location}
            imageUrl={result.imageUrl}
            audioUrl={result.audioUrl}
            referenceUrl={result.referenceUrl}
          />
        )}
      </div>
    </div>
  )
}
