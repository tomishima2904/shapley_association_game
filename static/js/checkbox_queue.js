const stim_dict = {
  "stimulus-1": "1",
  "stimulus-2": "2",
  "stimulus-3": "3",
  "stimulus-4": "4",
  "stimulus-5": "5",
};

// inputタグのうち type が checkbox のもの全てを対象
const checkboxes = document.querySelectorAll("input[type=checkbox]");

// 全ての checkbox に対して 'change' イベントを検知する
checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", handleCheckboxChange);
});

// チェックボックスの状態が変更されたときの処理を定義する関数
function handleCheckboxChange(event) {
  // 変化があった checkbox を取得
  var changed_checkbox = this;
  var changed_checkbox_id = stim_dict[changed_checkbox.id];

  // チェックが外された場合、リストから刺激語のidを削除
  if (queue.includes(changed_checkbox_id) === true) {
    var index = queue.indexOf(changed_checkbox_id);
    queue.splice(index, 1);

    // チェックが外されたチェックボックスの表示番号を削除
    var unchecked_checkbox_icon = document.getElementById("checkbox-icon-" + changed_checkbox_id);
    unchecked_checkbox_icon.classList.remove("checkbox-icon-checked");
    unchecked_checkbox_icon.classList.add("checkbox-icon");
    unchecked_checkbox_icon.innerText = "";

    // 全てのチェック済みチェックボックスの表示番号を付け替える
    if (queue.length > 0){
      for (let i=0; i<queue.length; i++){
        var checkbox_icon = document.getElementById("checkbox-icon-" + queue[i]);
        checkbox_icon.innerText = i + 1;
      }
    }
  }
  // チェックがされた場合、リストに刺激語のidを追加
  else {
    queue.push(changed_checkbox_id);
    // 今チェックされたチェックボックスに表示番号を付ける
    var checkbox_icon = document.getElementById("checkbox-icon-" + changed_checkbox_id);
    checkbox_icon.classList.remove("checkbox-icon");
    checkbox_icon.classList.add("checkbox-icon-checked");
    checkbox_icon.innerText = queue.indexOf(changed_checkbox_id) + 1;
  }
  console.log(queue);
}
