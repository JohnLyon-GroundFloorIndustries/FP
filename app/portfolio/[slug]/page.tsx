import {permanentRedirect} from 'next/navigation';export default async function Legacy({params}:{params:Promise<{slug:string}>}){const{slug}=await params;permanentRedirect('/work/'+slug)}
