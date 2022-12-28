import { queue } from './checkbox_queue.js';

// FetchAPI を使用するときは、CSRF に関する処理が必要になります。
const getCookie = (name) => {
	if (document.cookie && document.cookie !== '') {
		for (const cookie of document.cookie.split(';')) {
			const [key, value] = cookie.trim().split('=')
			if (key === name) {
				return decodeURIComponent(value)
			}
		}
	}
};
const csrftoken = getCookie('csrftoken');

// 解答する
const answer_form = document.getElementById('answer-form');
answer_form.addEventListener('submit', (e) => {
	e.preventDefault()
	const url = '{% url "gaming" %}'
	const answer = document.getElementById('user-answer')
	// URLのクエリパラメータを管理
	const body = new URLSearchParams()
	body.append('user-answer', answer.value)  // ユーザーの解答
    var u_order = queue.join('')  // こんな感じで刺激語の順序を文字列にしてdjango側に渡す
    body.append('u-order', u_order)  // ユーザーが選択した刺激語の順序

	// fetch API の登場! リロードしなくても画面の一部を更新できるようになる
	fetch('', {
		method: 'POST',
		body: body,
		// headersはCSRF 対策で必要なおまじない
		headers: {
		'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
		'X-CSRFToken': csrftoken,
		},
	})
		// viewからのデータをjsでJSON形式で受け取る
		.then((response) => {
			// JSON形式に変換
			return response.json()
		})
		.then((response) => {
			// フォームをクリア
			answer.value = ''
            // 刺激語を更新
			document.getElementById('label-stimulus-1').innerText = response.stimuli.stimulus_1
            document.getElementById('label-stimulus-2').innerText = response.stimuli.stimulus_2
            document.getElementById('label-stimulus-3').innerText = response.stimuli.stimulus_3
            document.getElementById('label-stimulus-4').innerText = response.stimuli.stimulus_4
            document.getElementById('label-stimulus-5').innerText = response.stimuli.stimulus_5
		})
	.catch((error) => {
			console.log(error)
	})
});
