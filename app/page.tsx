import Link from 'next/link'

export default function Home() {
  return (
    <section className="text-center mt-12">
      <h2 className="text-5xl font-semibold mb-6">Vielfalt für alle</h2>
      <p className="text-lg mb-8">
        Bei AIOS – Vielfalt für alle legen wir besonderen Wert auf Qualität und Kundenservice.
      </p>
      <Link
        href="/contact"
        className="inline-block px-6 py-3 border border-primary rounded-lg hover:bg-secondary text-white"
      >
        Kontakt aufnehmen
      </Link>
    </section>
  )
}
