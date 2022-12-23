let queue = [];
const stim_dict = {
    'stimulus-1': '1',
    'stimulus-2': '2',
    'stimulus-3': '3',
    'stimulus-4': '4',
    'stimulus-5': '5',
}

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
    var changed_checkbox_id = changed_checkbox.id;
    console.log(stim_dict[changed_checkbox_id]);

    // console.log(queue)
    // 以下、必要な処理を記述する
}

