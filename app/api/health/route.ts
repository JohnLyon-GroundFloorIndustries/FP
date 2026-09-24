import {db,json} from '../../lib/server';
export async function GET(){try{await db().prepare('SELECT 1').first();return json({status:'ok',storage:'available'})}catch{return json({status:'unavailable'},503)}}
