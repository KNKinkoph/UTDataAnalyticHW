// Homework:
// from data.js
var tableData = data;
var tablebody =  d3.select("tbody")
// Appends data 
// Add new row of data for each UFO sighting
// Make sure you have a column for `date/time`, `city`, `state`, `country`, `shape`, and `comment` at the very least.
// Build the table out:
function ufoTable(data){
tablebody.html("") 
data.forEach((datarow)=>{
    var row = tablebody.append("tr")
    Object.values(datarow).forEach((value)=>{
        var cell = row.append("td")
        cell.text(value)
    })   
})
}
ufoTable(tableData)

// Filter table

function filterTable(){
d3.event.preventDefault()
var date = d3.select("#datetime").property("value")
var filterData = tableData
if (date){
    filterData = filterData.filter(row=>row.datetime===date)
}
ufoTable(filterData)
}
// On click for the event of filter
d3.selectAll("#filter-btn").on("click", filterTable)


// Kaileigh Notes:
// Part 2: Drop down, in each option if/else if statment 
// city = value
// d3.event.preventDefault()
// var date = d3.select("#datetime").property("value")
// var filterData = tableData
// if (date){
//     filterData = filterData.filter(row=>row.datetime===date)