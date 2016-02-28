$(function() {
    navigator.getUserMedia = (navigator.getUserMedia ||
            navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia ||
            navigator.msGetUserMedia);
    var stream = undefined;
    navigator.getUserMedia ({
            video: false,
            audio: true
        },
        function success(localAudioStream) {
            stream = localAudioStream;
        },
        function error(err) {
            alert("Cannot access microphone");
        }
    );
    var me = new Peer({key: "y2hctf90xq63l3di"});
    me.on('call', function(incoming) {
        incoming.on('stream', function(stream) {
            var audio = $('<audio autoplay />').appendTo('body');
            audio[0].src = (URL || webkitURL || mozURL).createObjectURL(stream);
        }
    });
    $("#guide").on("click", function () {
        $.post({
            url: "/add_guide"
            data: {"peerjs":me.id},
            success: function(data) {
                // TODO Update counter
            }
        });
    });

    $("tourist").on("click", function () {
        $.ajax({
            url: "/tourist",
            success: function(peer) {
                var outgoing = me.call(peer, stream);
                outgoing.on('stream', function(stream) {
                    var audio = $('<audio autoplay />').appendTo('body');
                    audio[0].src = (URL || webkitURL || mozURL).createObjectURL(stream);
                });
            }
    });
});
