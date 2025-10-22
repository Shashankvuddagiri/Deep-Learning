import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Brain, Camera, Book, Volume2, Globe, History } from 'lucide-react'

export function About() {
  return (
    <div className="space-y-8">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold">About ChronoScope</h1>
        <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
          ChronoScope is an intelligent historical image detection and storytelling platform 
          that transforms static images into interactive historical narratives.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <CardHeader>
            <Brain className="h-8 w-8 text-primary mb-2" />
            <CardTitle>AI Recognition</CardTitle>
            <CardDescription>
              Advanced CNN/ViT + CLIP models for accurate historical landmark detection
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              Our AI models can identify historical monuments, artifacts, and landmarks 
              with high accuracy, providing confidence scores for each prediction.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <Book className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Knowledge Retrieval</CardTitle>
            <CardDescription>
              Wikipedia and Wikidata integration for verified historical information
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              We fetch comprehensive historical data including construction dates, 
              locations, architectural details, and cultural significance.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <Volume2 className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Audio Narration</CardTitle>
            <CardDescription>
              Text-to-speech technology for immersive storytelling
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              Listen to historical stories with natural-sounding narration, 
              making history accessible to everyone.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <Camera className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Image Analysis</CardTitle>
            <CardDescription>
              Support for various image formats and quality levels
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              Upload photos in JPG, PNG, GIF, or WebP formats. Our system 
              works with both modern and historical photographs.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <Globe className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Global Coverage</CardTitle>
            <CardDescription>
              Recognition of landmarks from around the world
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              From ancient pyramids to modern monuments, our database 
              includes historical sites from every continent.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <History className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Historical Context</CardTitle>
            <CardDescription>
              Rich historical narratives and cultural significance
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              Learn about the historical context, architectural significance, 
              and cultural importance of each recognized landmark.
            </p>
          </CardContent>
        </Card>
      </div>

      <div className="bg-muted/50 rounded-lg p-8 text-center">
        <h2 className="text-2xl font-bold mb-4">How It Works</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="space-y-2">
            <div className="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto text-lg font-bold">1</div>
            <h3 className="font-semibold">Upload Image</h3>
            <p className="text-sm text-muted-foreground">Upload a photo of a historical landmark or artifact</p>
          </div>
          <div className="space-y-2">
            <div className="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto text-lg font-bold">2</div>
            <h3 className="font-semibold">AI Analysis</h3>
            <p className="text-sm text-muted-foreground">Our AI models identify the landmark and extract features</p>
          </div>
          <div className="space-y-2">
            <div className="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto text-lg font-bold">3</div>
            <h3 className="font-semibold">Data Retrieval</h3>
            <p className="text-sm text-muted-foreground">Fetch historical information from Wikipedia and Wikidata</p>
          </div>
          <div className="space-y-2">
            <div className="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto text-lg font-bold">4</div>
            <h3 className="font-semibold">Story Creation</h3>
            <p className="text-sm text-muted-foreground">Generate narrative and audio for interactive storytelling</p>
          </div>
        </div>
      </div>
    </div>
  )
}
