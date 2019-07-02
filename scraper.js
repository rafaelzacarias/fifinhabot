// Run the following script in webpages [1], [2] and [3] and save the
// results in "teams.csv", "men_nationals.csv" and "women_national.csv".
//
// [1] https://www.fifaindex.com/teams
// [2] https://www.fifaindex.com/teams/?type=1
// [3] https://www.fifaindex.com/teams/?type=2

$('table.table-teams tbody tr').each(function(i, e) {
  var name = $(e).find('td[data-title="Name"]>a:first').text();
  var star = $(e).find('td[data-title="Team Rating"]>span>i.fas.fa-star').length;
  var halfStar = $(e).find('td[data-title="Team Rating"]>span>i.fas.fa-star-half-alt').length;
  var rating = star + 0.5 * halfStar;
  console.log(name + ',' + rating);
});
