var queue = [];
const stim_dict = {
    'stimulus-1': '1',
    'stimulus-2': '2',
    'stimulus-3': '3',
    'stimulus-4': '4',
    'stimulus-5': '5',
};

// inputタグのうち type が checkbox のもの全てを対象
const checkboxes = document.querySelectorAll('input[type=checkbox]');

// 全ての checkbox に対して 'change' イベントを検知する
checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', handleCheckboxChange);
});

// チェックボックスの状態が変更されたときの処理を定義する関数
function handleCheckboxChange(event) {

    // 変化があった checkbox を取得
    var changed_checkbox = this;
    var changed_checkbox_id = stim_dict[changed_checkbox.id];

    // チェックが外された場合、リストから刺激語のidを削除
    if (queue.includes(changed_checkbox_id) === true){
        var index = queue.indexOf(changed_checkbox_id)
        queue.splice(index, 1)
    }
    // チェックがされた場合、リストに刺激語のidを追加
    else{
        queue.push(changed_checkbox_id)
    }
    console.log(queue);
};

export {queue};  // queue 変数を fetch.js で使えるようにする
