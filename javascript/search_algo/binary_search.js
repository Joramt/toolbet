let binary_search = function (arrayToSearch, valueToFind, searchRangeBeginning, searchRangeEnd) {

    if(searchRangeBeginning > searchRangeEnd)
        return false;
    
    window.binarySearchIteration++;
    let searchRange = searchRangeBeginning + searchRangeEnd;
    let searchRangeMiddle = Math.floor( searchRange /2);
    let valueMiddle = arrayToSearch[searchRangeMiddle];

    console.log(valueToFind)
    console.log(valueMiddle)
    console.log(parseInt(valueToFind) < parseInt(valueMiddle))
    console.log("=======")
    if(valueMiddle === valueToFind)
        return true;

    if(parseInt(valueToFind) < parseInt(valueMiddle))
        return binary_search(arrayToSearch, valueToFind, searchRangeBeginning, searchRangeMiddle - 1)
    else 
        return binary_search(arrayToSearch, valueToFind, searchRangeMiddle + 1, searchRangeEnd)
    

}


window.binary_search = binary_search;
