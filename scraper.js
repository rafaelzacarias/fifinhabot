// Run the following script in webpage https://www.fifaindex.com/teams,
// copy the results and save in the file "teams.csv"

$('table.teams tbody tr').each(function(i, e) {
  var name = $(e).find('td[data-title="Name"]>a:first').text();
  var star = $(e).find('td[data-title="Team Rating"]>span>i.fa-star').length;
  var halfStar = $(e).find('td[data-title="Team Rating"]>span>i.fa-star-half-o').length;
  var rating = star + 0.5 * halfStar;
  console.log(name + ',' + rating);
});
