import request from '@/utils/request'

export function getList() {
  return request({
    url: '/api/show_books',
    method: 'get',
  })
 }

export function addbook(book_name,phone,relation,address,money) {
  return request({
    url: '/api/add_book',
    method: 'get',
    params: { book_name,phone,relation,address,money }
  })
}

export function deletebook(book_name) {
  return request({
    url: '/api/delete_book',
    method: 'get',
    params: { book_name }
  })
}

export function updatebook(book_name,phone,relation,address,money) {
  return request({
    url: '/api/update_book',
    method: 'get',
    params: { book_name,phone,relation,address,money }
  })
}
