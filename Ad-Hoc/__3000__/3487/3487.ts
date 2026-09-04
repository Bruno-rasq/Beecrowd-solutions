const input: string[] = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const segment_s: string = input.shift()
const segment_p: string = input.shift()

const removeAllOccur = (s: string, p: string): string => {
    const pos: number = s.indexOf(p);
    if (pos === -1) {
        return s.length === 0 ? "null value" : s;
    }
    const nova: string = s.slice(0, pos) + s.slice(pos + p.length);
    return removeAllOccur(nova, p);
};

const ans: string = removeAllOccur(segment_s, segment_p);
console.log(ans);