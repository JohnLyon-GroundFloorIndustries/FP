import {env} from 'cloudflare:workers';
import type { Metadata } from "next";
import "./globals.css";
import Header from './components/header';
import Footer from './components/footer';
import Consent from './components/consent';

export const metadata: Metadata = {
  robots:env.INDEXING_ENABLED==='true'?{index:true,follow:true}:{index:false,follow:false},
  metadataBase: new URL('https://flora-pacifica-updated.johnlyon.chatgpt.site'),
  title: {default:'Washington Wedding Florist | Flora Pacifica',template:'%s | Flora Pacifica'},
  description: 'Full-service floral design for weddings and private celebrations across Washington and the Pacific Northwest.',
  openGraph: {siteName:'Flora Pacifica',type:'website',images:[{url:'/images/hero.webp',alt:'Flora Pacifica wedding floral design'}]},twitter:{card:'summary_large_image',images:['/images/hero.webp']},
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body><script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify({'@context':'https://schema.org','@type':'Organization',name:'Flora Pacifica',url:'https://flora-pacifica-updated.johnlyon.chatgpt.site',sameAs:['https://www.instagram.com/florapacifica.co/','https://www.pinterest.com/florapacificaco/','https://www.facebook.com/florapacificafloralco']})}}/><Header/>{children}<Footer/><Consent/></body>
    </html>
  );
}
