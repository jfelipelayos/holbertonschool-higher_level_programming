$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json'
  }).done((character) => {
    $('#character').text(character.name);
  });
});
