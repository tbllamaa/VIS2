var spec2 = "bar_volc.json";
vegaEmbed('#bar1', spec2, { actions: false }).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);