function buildMetadata(sample) {
  var url = '/metadata/' + sample;
  // @TODO: Complete the following function that builds the metadata panel
  console.log("sample", sample)
  // Use `d3.json` to fetch the metadata for a sample
  d3.json(url).then(function (data) {
    var selector = d3.select("#sample-metadata");
  // Use `.html("") to clear any existing metadata
  selector.html("");
  // Use `Object.entries` to add each key and value pair to the panel
  Object.entries(data).forEach(([key, value]) => {
 // Hint: Inside the loop, you will need to use d3 to append new
 // tags for each key-value in the metadata. ES6 syntax to add into like for i, i<10, i++ shorthand forEach
  selector.append("h6").text(`${key}: ${value}`)
    });
  });
}

 // @TODO: Build a Pie Chart&Bubble Chart - otu_ids for the label and sample_values for values in pie chart 

function init() {
function buildCharts(sample) {
  var url = '/samples/' + sample;
  console.log("sample", sample)
 
  d3.json(url).then(function (data) {
  
     var otu_ids = data.otu_ids
     var sample_values = data.sample_values
     var labels = data.otu_labels
     var pie_chart = [
       {
        values: sample_values.slice(0,10),
        labels: otu_ids.slice(0,10),
        hovertext: labels.slice(0,10),
        type: "pie"
       }
     ]
     var layout = {
      height: 600,
      width: 800,
      margin: { t: 0, l: 0 }
    };
    Plotly.plot("pie", pie_chart, layout);
    var bubble_chart = [
      {
        x: otu_ids,
        y: sample_values,
        text: labels,
        mode: "markers",
        marker: {
          size: sample_values, 
          colors: otu_ids, 
          colorscale: "Earth"
        }
      }
    ]
    var layout_bubble = {
      margin: { t: 0}, 
      hovermode: "closest",
      xaxis: {
        title: "OTU ID"
      }

    }
    Plotly.plot("bubble", bubble_chart, layout_bubble);
    }) 
  }
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
