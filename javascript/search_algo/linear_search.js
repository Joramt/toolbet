// Complexity O(n) since in the worst case ( value at the end of array ) we have to parse the whole array
// Works on sorted and unsorted array

let linear_search = function (arrayToSearch, valueToFind) {

    let isFound = false;
    for(let i = 0; i <= arrayToSearch.length; i++){
        window.linearSearchIteration++;
        if(arrayToSearch[i] === valueToFind){
            isFound = true;
            break;
        }
    }

    return isFound;
}


window.linear_search = linear_search;
