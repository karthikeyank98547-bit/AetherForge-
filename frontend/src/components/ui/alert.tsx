import {cn} from '@/lib/utils';export function Alert({className,...p}:React.HTMLAttributes<HTMLDivElement>){return <div {...p} className={cn('rounded-2xl border p-4 bg-white',className)}/>} 
