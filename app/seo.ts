import type {Metadata} from 'next';
import {origin} from './content';
export function pageMetadata(title:string,description:string,path:string,image='hero'):Metadata{return {title,description,alternates:{canonical:path},openGraph:{title:title+' | Flora Pacifica',description,url:origin+path,siteName:'Flora Pacifica',type:'website',images:[{url:origin+'/images/'+image+'.webp',alt:'Flora Pacifica floral design'}]},twitter:{card:'summary_large_image',title:title+' | Flora Pacifica',description,images:[origin+'/images/'+image+'.webp']}};}
