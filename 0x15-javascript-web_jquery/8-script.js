$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const items = [];
  $.each(data.results, function (key, val) {
    console.log('key', val);
    items.push('<li>' + val.title + '</li>');
  });
  $('UL#list_movies').append(items.join(''));
});
