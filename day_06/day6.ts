process.stdin.on('data', data => {
    data.toString().split('\r\n').filter(o=>o).map(x => {console.log( {"Part1": day6.parseBuffer(x,4), "Part2" : day6.parseBuffer(x,14)} )});
    process.exit();
  });

class day6 {  
    static isMarker(text:string): boolean {
        return text.length == new Set(text).size
    }

    static parseBuffer(buffer:string, l:number) : number {
        for( let i=0; i < buffer.length-l; i++){
            if(day6.isMarker(buffer.slice(i,i+l))) return i + l   
        }
        return 0
    }
}

//cat .\input.txt | npx ts-node .\day6.ts 