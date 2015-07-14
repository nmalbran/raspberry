
(function(){
    var app = angular.module('weather', []);

    app.controller('temperatureController', ['$http', function($http){
        var weatherData = this;
        weatherData.temperature = "-";
        weatherData.humidity = "-";
        weatherData.timestamp = "-";

        this.updateTemperature = function(){
            $http.get('/api/cur').success(function(data){
                weatherData.temperature = data.data.temperature;
                weatherData.humidity = data.data.humidity;
                weatherData.timestamp = data.data.timestamp;
            });
        };
        this.updateTemperature();
    }]);

    app.controller('panelController', function(){
        this.tab = 1;
        this.selectTab = function(setTab){
            this.tab = setTab;
        };
        this.isSelected = function(checkTab){
            return this.tab === checkTab;
        };
    });

    app.controller('graphController', ['$http', function($http){
        var options = {
            animation: false,
            showTooltips: false,
            bezierCurve : true,
            responsive: true,
            pointDot: false,
            datasetFill: false,
            scaleOverride: true,
            scaleStartValue: 14,
            scaleStepWidth: 1,
            scaleSteps: 11,
            scaleShowGridLines: true,
        };

        this.buildGraph = function(ctx, url, options){
            $http.get(url).success(function(data){
                var graphData = {
                    labels: data.data.timestamp,
                    datasets: [
                        {
                            label: "Avg",
                            data: data.data.avg,
                            strokeColor: "rgba(0,255,0,0.7)",
                        },
                        {
                            label: "Min",
                            data: data.data.min,
                            strokeColor: "rgba(0,0,255,0.7)",
                        },
                        {
                            label: "Max",
                            data: data.data.max,
                            strokeColor: "rgba(255,0,0,0.7)",
                        }
                    ]
                };
                return new Chart(ctx).Line(graphData, options);
            });
        };

        var dayCtx = $("#dayGraph").get(0).getContext("2d");
        var dayGraph = this.buildGraph(dayCtx, '/api/day', options);

        var weekCtx = $("#weekGraph").get(0).getContext("2d");
        var weekGraph = this.buildGraph(weekCtx, '/api/week', options);

        var monthCtx = $("#monthGraph").get(0).getContext("2d");
        var monthGraph = this.buildGraph(monthCtx, '/api/month', options);
    }]);

})();
