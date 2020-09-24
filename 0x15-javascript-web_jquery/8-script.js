$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json'
  }).done((movies) => {
    for (const movie of movies.results) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    }
  });
});
