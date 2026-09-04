const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const segment_s = input.shift()
const segment_p = input.shift()

const removeAllOccur = (s, p) => {
    const pos = s.indexOf(p);
    if (pos === -1) {
        console.log(s.length === 0 ? "null value" : s);
        return;
    }
    const nova = s.slice(0, pos) + s.slice(pos + p.length);
    removeAllOccur(nova, p);
};

removeAllOccur(segment_s, segment_p);