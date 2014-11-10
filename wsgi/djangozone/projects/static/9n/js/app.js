(function(){
  var app = angular.module('cartomap', ['ui.bootstrap']);
  app.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
  });

  app.controller('TabController', function(){
  });

  var colors = { 'S\xED - S\xED': '#3B7522',
                 'S\xED - No': '#E18925',
                 'No': '#C1001A',
                 'En blanc': '#FFFFCC',
                 'Altres': '#66298E',
                 'S\xED - En blanc': '#0066CC', }

  app.directive('stats', function() {

    return {
      restrict: 'E',
      templateUrl: '/projects/9n/stats.html',
      controllerAs: 'stats',
      controller: function() {
        this.colors = colors;
        this.vots = [];
        this.percent_vots = {'total': 0};
      },
      link: function (scope, element, attrs) {
        scope.$watch("stats.vots", function(newValue, oldValue) {
          scope.stats.percent_vots['total'] = 0;
          scope.stats.vots.forEach(function (e) {
            scope.stats.percent_vots[e.sigles] = e.percent;
          });
        });
      },
    };
  });

  app.directive('pieChart', function() {
    var width = 450,
        height = 400,
        radius = Math.min(width, height) / 2;

    return {
      restrict: 'E',
      scope: {
        data: '='
      },
      link: function (scope, element, attrs) {

        var arc = d3.svg.arc()
            .outerRadius(radius - 10)
            .innerRadius(0);


        var pie = d3.layout.pie()
            .value(function(d) { return d.vots; })
            .sort(null);

        // var arc = d3.svg.arc()
        //   .innerRadius(radius - 100)
        //   .outerRadius(radius - 20);

        var svg = d3.select(element[0])
            .append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

        var path;

        scope.render = function(data) {

          var root = data.slice();

          root.forEach(function(d) {
            d.vots = +d.vots;
          });

          if (path==undefined) {
            path = svg.selectAll("path")
                .data(pie(root))
                .enter().append("path")
                .attr("idc", function(d) { d.data.sigles.trim() })
                .attr("fill", function(d) { return colors[d.data.sigles.trim()]; })
                .attr("stroke", "#fff")
                .attr("d", arc)
                .each(function(d) { this._current = d });

          } else {

            path = path.data(pie(root)); // compute the new angles
            path.transition().duration(100).attrTween("d", arcTween); // redraw the arcs
          }

        }
        scope.$watch('data', function(newVal, oldVal){
          if (newVal!=undefined) {
            scope.render(newVal);
          }
        }, true);

        function arcTween(a) {
          var i = d3.interpolate(this._current, a);
          this._current = i(0);
          return function(t) {
            return arc(i(t));
          };
        }

      }
    };

  });

  app.directive('mapCanvas', ['$compile', function ($compile) {
    var width = 790, height = 570;

    return {
      restrict: 'A',
      controllerAs: 'map',
      controller: function() {
        this.comarca_str = "";
        this.comarca_color = "";
        this.vote_data;
        this.ndata = {};
        this.lol = {}
      },

      link: function (scope, element, attrs) {
        scope.setOnHoverData = function(name, element_id) {
          scope.map.comarca_str = name;
          scope.map.vote_data = scope.map.ndata[parseInt(element_id)].slice();
          scope.map.comarca_color = colors[scope.map.vote_data[0].sigles.trim()];
          scope.stats.vots = scope.map.vote_data.slice();
          scope.stats.vots.sort(function(a,b) {
            return a.vots < b.vots;
          });
        }

        var projection = d3.geo.mercator()
            .center([2.3,41.7])
            .scale(10500)
            .translate([width / 2, height / 2]);

        var path = d3.geo.path()
            .projection(projection);

        var svg = d3.select(element[0]).append("svg")
            .attr("width", width)
            .attr("height", height);

        var geodata;
        var data;

        d3.csv("/static/9n/data/9n.csv", function(d) {
          return {
            sigles: d.Sigles,
            vots: +d.Vots,
            comarca: +d["Codi Comarca"],
            percent: d.percent,
          };
        }, function(error, rows) {
          data=d3.nest()
            .key(function(d) {return parseInt(d.comarca);})
            .sortKeys(d3.ascending)
            .entries(rows);
          data.forEach(function(e) {
            scope.map.ndata[e.key] = e.values;
          });

          //Wait for votes parsing before displaying the map
          d3.json("/static/9n/data/geo/comarques.topo.json", function(error, cat) {
            geodata = topojson.feature(cat, cat.objects.comarques).features;
            showData();
          });
        });

        var showData = function() {
          comarques = svg.selectAll(".comarca")
            .data(geodata)
            .enter().append("path")
            .attr("id", function(d) {
              return d.properties.comarca;
            })
            .attr("ng-mouseover", function(d) {
              return "setOnHoverData('"+String(d.properties.comarca_str).replace("'", "\\\'")+"', '"+d.properties.comarca+"')";
            })
            .attr("fill", function(d) { return colors[scope.map.ndata[parseInt(d.properties.comarca)][0].sigles.trim()]; })
            .attr("class", "comarca")
            .attr("d", path)


          element.removeAttr("map-canvas");
          $compile(element)(scope);
        }

      }

    };
  }]);

})();
