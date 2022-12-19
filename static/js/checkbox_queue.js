let a = 0

// inputタグのうち type が checkbox のもの全てを対象
const checkboxes = document.querySelectorAll('input[type=checkbox]');

// 全ての checkbox に対して 'change' イベントを検知する
checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', handleCheckboxChange);
});

// チェックボックスの状態が変更されたときの処理を定義する関数
function handleCheckboxChange(event) {
    console.log(a); // チェックされている場合はtrue、されていない場合はfalse
    a += 1;
    // 以下、必要な処理を記述する
}
