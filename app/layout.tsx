// app/layout.tsx
import './globals.css'
import Image from 'next/image'
import Link from 'next/link'

export const metadata = {
  title: 'AIOS Geisenheim',
  description: 'Offizielle Web-App für AIOS Geisenheim',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="de">
      <body className="bg-black text-white min-h-screen flex flex-col">
        {/* Header */}
        <header className="w-full bg-black text-white">
          <div className="max-w-4xl mx-auto flex justify-between items-center py-4 px-4">
            <Image
              src="/images/logo.png"
              alt="AIOS Geisenheim Logo"
              width={200}
              height={60}
            />
            <nav className="space-x-6">
              <Link href="/">Home</Link>
              <Link href="/about">Über uns</Link>
              <Link href="/services">Dienstleistungen</Link>
              <Link href="/contact">Kontakt</Link>
              <Link href="/impressum">Impressum</Link>
            </nav>
          </div>
        </header>

        {/* Seiteninhalt */}
        <main className="flex-1 w-full max-w-4xl mx-auto px-4 py-8">
          {children}
        </main>

        {/* Footer */}
        <footer className="w-full bg-black text-gray-400 py-6 mt-auto">
          <div className="max-w-4xl mx-auto text-center text-sm px-4">
            <p>
              <strong>Email:</strong> info@aios-geisenheim.de&nbsp;|&nbsp;
              <strong>Telefon:</strong> 06722 4149377
            </p>
            <p>© {new Date().getFullYear()} AIOS Geisenheim</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
