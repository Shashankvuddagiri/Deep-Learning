import { Link, useLocation } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { History, Home, Info, Compass } from 'lucide-react'

export function Navbar() {
  const location = useLocation()

  const isActive = (path: string) => location.pathname === path

  return (
    <nav className="border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto px-4">
        <div className="flex h-16 items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="flex items-center space-x-2">
              <div className="h-8 w-8 rounded-lg bg-primary flex items-center justify-center">
                <span className="text-primary-foreground font-bold text-sm">CS</span>
              </div>
              <span className="text-xl font-bold">ChronoScope</span>
            </div>
          </div>
          
          <div className="flex items-center space-x-1">
            <Button
              variant={isActive('/') ? 'default' : 'ghost'}
              size="sm"
              asChild
            >
              <Link to="/" className="flex items-center space-x-2">
                <Home className="h-4 w-4" />
                <span>Home</span>
              </Link>
            </Button>
            
            <Button
              variant={isActive('/explore') ? 'default' : 'ghost'}
              size="sm"
              asChild
            >
              <Link to="/explore" className="flex items-center space-x-2">
                <Compass className="h-4 w-4" />
                <span>Explore</span>
              </Link>
            </Button>
            
            <Button
              variant={isActive('/history') ? 'default' : 'ghost'}
              size="sm"
              asChild
            >
              <Link to="/history" className="flex items-center space-x-2">
                <History className="h-4 w-4" />
                <span>History</span>
              </Link>
            </Button>
            
            <Button
              variant={isActive('/about') ? 'default' : 'ghost'}
              size="sm"
              asChild
            >
              <Link to="/about" className="flex items-center space-x-2">
                <Info className="h-4 w-4" />
                <span>About</span>
              </Link>
            </Button>
          </div>
        </div>
      </div>
    </nav>
  )
}
