/* 
  아래에 코드를 작성해주세요.
  
*/




const searchBtn = document.querySelector('.search-box__button')

function fetchAlbums(page = 1, limit = 10) {
  const keyword = document.querySelector('.search-box__input').value
  axios({
    method : 'get',
    url : 'http://ws.audioscrobbler.com/2.0',
    params : {
      method : 'album.search',
      album : keyword,
      api_key : `ada341d122a4264e2f02da197c28483b`,
      format : 'json',
    }
  })
  .then((response) => {
    const result = document.querySelector('.search-result')
    const albums = document.createElement('div')
    result.appendChild(albums)

    let lst = response.data.results.albummatches.album
    lst.forEach(element => {

      const div1 = document.createElement('div')
      div1.classList.add('search-result__card')

      const img = document.createElement('img')
      img.src = element.image[1]['#text']
      console.log(img)

      const div2 = document.createElement('div')
      div2.classList.add('search-result__text')

      const h2 = document.createElement('h2')
      h2.innerText = element['artist']

      const p = document.createElement('p')
      p.innerText = element['name']


      div2.append(h2,p)
      div1.append(img,div2)
      albums.append(div1)
      
    });

  })
  .catch((error) => {
    alert('다시 시도해주세요')
  })
}
searchBtn.addEventListener('click',  fetchAlbums)
