window.onload = function() {

    const ANIMATION_SPEED = 100;

    $("div[id$='_form']").hover(
        function() {
            $("#" + this.id.replace('form', 'help'))
                .animate({
                    opacity: 1
                }, ANIMATION_SPEED);
        },
        function () {
            $("#" + this.id.replace('form', 'help'))
                .animate({
                    opacity: 0
                }, ANIMATION_SPEED);
        }
    )

};