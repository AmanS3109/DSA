const squaredArray = (array) => {
    // let sortedSquare = new Array(array.length).fill(0);
    // for (let index = 0; index < array.length; index++) {
    //     value = array[index];
    //     sortedSquare[index] = value + value;
    // Array.prototype.sort(sortedSquare);
    // return sortedSquare;
    // }
    let sortedSquare = array.map(num => num * num); // Calculate squares of elements
    sortedSquare.sort((a, b) => a - b); // Sort the squared elements in ascending order
    return sortedSquare;
}
// O(nlogn)

let array = [-4, -2, 1, 3, 9]
console.log(squaredArray(array))