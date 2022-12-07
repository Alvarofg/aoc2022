process.stdin.on('data', data => {
    console.log(data.toString().split('\r\n').filter(o=>o).map(parseBuffer));
    process.exit();
  });

function isMarker(text){
    return text.length == new Set(text).size
}

function parseBuffer(buffer){
    for( let i=0; i < buffer.length-4; i++){
        if(isMarker(buffer.slice(i,i+4))) return i + 4   
    }
}