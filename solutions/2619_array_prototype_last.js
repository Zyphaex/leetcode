/* 
LeetCode Problem: 
2619. Array Prototype Last

Write code that enhances all arrays such that you can call the array.last() method on any array and it will 
return the last element. If there are no elements in the array, it should return -1.

You may assume the array is the output of JSON.parse.
*/

Array.prototype.last = function() {
    return this.length ? this.slice(-1)[0] : -1;
};