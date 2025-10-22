import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Play, Pause, Volume2, ExternalLink, MapPin, Calendar } from 'lucide-react'
import { useState } from 'react'

interface ResultCardProps {
  landmark: string
  confidence: number
  summary: string
  yearBuilt?: string
  location?: string
  imageUrl?: string
  audioUrl?: string
  referenceUrl?: string
}

export function ResultCard({
  landmark,
  confidence,
  summary,
  yearBuilt,
  location,
  imageUrl,
  audioUrl,
  referenceUrl
}: ResultCardProps) {
  const [isPlaying, setIsPlaying] = useState(false)
  const [audio, setAudio] = useState<HTMLAudioElement | null>(null)

  const handlePlayAudio = () => {
    if (audioUrl) {
      if (isPlaying && audio) {
        audio.pause()
        setIsPlaying(false)
      } else {
        const newAudio = new Audio(audioUrl)
        newAudio.onended = () => setIsPlaying(false)
        newAudio.play()
        setAudio(newAudio)
        setIsPlaying(true)
      }
    }
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

  return (
    <Card className="w-full max-w-4xl mx-auto">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="space-y-2">
            <CardTitle className="text-2xl">{landmark}</CardTitle>
            <div className="flex items-center space-x-4">
              <Badge 
                variant="secondary" 
                className={`${getConfidenceColor(confidence)} text-white`}
              >
                {getConfidenceText(confidence)} Confidence
              </Badge>
              <span className="text-sm text-muted-foreground">
                {(confidence * 100).toFixed(1)}%
              </span>
            </div>
          </div>
          {audioUrl && (
            <Button
              variant="outline"
              size="sm"
              onClick={handlePlayAudio}
              className="flex items-center space-x-2"
            >
              {isPlaying ? (
                <Pause className="h-4 w-4" />
              ) : (
                <Play className="h-4 w-4" />
              )}
              <Volume2 className="h-4 w-4" />
            </Button>
          )}
        </div>
      </CardHeader>
      
      <CardContent className="space-y-6">
        {imageUrl && (
          <div className="flex justify-center">
            <img
              src={imageUrl}
              alt={landmark}
              className="max-w-full h-auto rounded-lg shadow-md max-h-96 object-cover"
            />
          </div>
        )}
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {yearBuilt && (
            <div className="flex items-center space-x-2">
              <Calendar className="h-4 w-4 text-muted-foreground" />
              <span className="text-sm font-medium">Built:</span>
              <span className="text-sm">{yearBuilt}</span>
            </div>
          )}
          
          {location && (
            <div className="flex items-center space-x-2">
              <MapPin className="h-4 w-4 text-muted-foreground" />
              <span className="text-sm font-medium">Location:</span>
              <span className="text-sm">{location}</span>
            </div>
          )}
        </div>
        
        <div className="space-y-2">
          <h4 className="font-semibold">Historical Summary</h4>
          <CardDescription className="text-base leading-relaxed">
            {summary}
          </CardDescription>
        </div>
        
        {referenceUrl && (
          <div className="pt-4 border-t">
            <Button variant="outline" asChild>
              <a
                href={referenceUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center space-x-2"
              >
                <ExternalLink className="h-4 w-4" />
                <span>Learn More on Wikipedia</span>
              </a>
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  )
}
