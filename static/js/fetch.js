import { queue } from "./checkbox_queue.js";

// FetchAPI を使用するときは、CSRF に関する処理が必要になります。
const getCookie = (name) => {
  if (document.cookie && document.cookie !== "") {
    for (const cookie of document.cookie.split(";")) {
      const [key, value] = cookie.trim().split("=");
      if (key === name) {
        return decodeURIComponent(value);
      }
    }
  }
};
const csrftoken = getCookie("csrftoken");

// 解答する
const answer_form = document.getElementById("answer-form");
const NUM_STIM = 5;
answer_form.addEventListener("submit", (e) => {
  e.preventDefault(); // フォームの送信をキャンセルする

  // 全ての刺激語がチェックされている場合は、フォームを送信する
  if (queue.length >= NUM_STIM) {

    const url = '{% url "gaming" %}';
    const answer = document.getElementById("user-answer");
		const checkboxes = document.getElementsByName('stimulus');
		const checkbox_labels = document.getElementsByName('label-stimulus');

    // URLのクエリパラメータを管理
    const body = new URLSearchParams();
    body.append("user-answer", answer.value); // ユーザーの解答
    const u_order = queue.join(""); // こんな感じで刺激語の順序を文字列にしてdjango側に渡す
    body.append("u-order", u_order); // ユーザーが選択した刺激語の順序
		body.append("left-questions", left_questions);

    // fetch API の登場! リロードしなくても画面の一部を更新できるようになる
    fetch("", {
      method: "POST",
      body: body,
      // headersはCSRF 対策で必要なおまじない
      headers: {
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "X-CSRFToken": csrftoken,
      },
    })
      // viewからのデータをjsでJSON形式で受け取る
      .then((response) => {
        // JSON形式に変換
        return response.json();
      })
      .then((response) => {
        // フォームをクリア
        answer.value = "";
        // 刺激語を更新 & チェクボックスをクリアな状態に
				for (let i=0; i<NUM_STIM; i++){
					checkbox_labels[i].innerText = response.stimuli[i];
					// checkboxes[i].checked = false;  バグるためコメントアウトしておく
				}
				// ユーザーが答えなければいけない質問数を更新する
				left_questions = response.left_questions;
				// ユーザーが選択した刺激語の順序を記憶する配列もクリアに
				queue = [];
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    alert("全ての刺激語を選択してください");
    console.log("全ての刺激語を選択してください");
  }
});
