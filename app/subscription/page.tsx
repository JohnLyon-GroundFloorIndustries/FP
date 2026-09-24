import Choice from './choice';import {PageHero} from '../components/shared';
export const metadata={title:'Your Email Preferences',robots:{index:false,follow:false}};
export default function Subscription(){return <main id="main-content"><PageHero eyebrow="YOUR INBOX, YOUR CHOICE" title="Email preferences."/><section className="section"><Choice/></section></main>}
