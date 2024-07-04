let isUnique = (str) => {
    str = str.toLowerCase();
    if (str.length > 128) {
        return false;
    }
    let charSet = new Array(128).fill(false);
    for (let i = 0; i < str.length; i++) {
        let val = str.charCodeAt(i);
        if (charSet[val]) {
            return false;
        }
        charSet[val] = true;
    }
    return true;
}
let str = "Aman";
console.log(isUnique(str))