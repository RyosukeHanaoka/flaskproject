document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('#imageContainer .checkbox');
    checkboxes.forEach(function(checkbox) {
        const x = checkbox.dataset.x; // ここは変更なし
        const y = checkbox.dataset.y; // ここは変更なし
        checkbox.style.left = x; // 'px' の追加を削除して、データ属性から直接値を設定
        checkbox.style.top = y; // 同上
    });
});

