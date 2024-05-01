// Получаем ссылки на элементы на странице
var searchInput = document.getElementById('srch');
var searchButton = document.querySelector('.search-box button');

// Добавляем обработчик события клика на кнопку поиска
searchButton.addEventListener('click', function() {
  // Получаем текст из поля ввода
  var searchText = searchInput.value.toLowerCase();

  // Получаем все элементы на странице, в которых есть текстовое содержимое
  var elements = document.querySelectorAll('body *:not(script):not(style)');

  // Проходимся по всем элементам и проверяем содержимое на соответствие поисковому запросу
  for (var i = 0; i < elements.length; i++) {
    var element = elements[i];
    var elementText = element.innerText.toLowerCase();

    // Если текст элемента содержит поисковый запрос, делаем его видимым
    if (elementText.includes(searchText)) {
      element.style.display = 'block';
    } else {
      // Если текст элемента не содержит поисковый запрос, скрываем его
      element.style.display = 'none';
    }
  }
});