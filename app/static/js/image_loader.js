<script>

cosole.log('script loaded');

            var btnFile = document.getElementById("inputImage");

            //Register event on file selected or changed.
            addEvents(btnFile, "change", function (event) {
                if (event.target.files.length !== 0) {
                    cosole.log('worked');
                    var file = event.target.files[0];
                    //Check if the file is IMAGE.
                    if (file.type.match("image.*")) {

                        var fl = new FileReader();

                        //Add event to read the content file.
                        addEvents(fl, "load", function (evt) {
                            //alert(evt.target.result);
                            try {


                                //CONVERT ARRAY BUFFER TO BASE64 STRING.
                                var dataURL = evt.target.result;
                                cosole.log(dataURL);
                                document.getElementById("filmMainImage").src = dataURL;


                            } catch (e) {
                                alert(e);
                            }

                        });

                        //Read the file as arraybuffer.

                        fl.readAsDataURL(file);

                    } else {

                        alert("Please select a IMAGE FILE");
                    }
                }

            });

            function addEvents(obj, evtName, func) {
                if (obj.addEventListener !== undefined && obj.addEventListener !== null) {
                    obj.addEventListener(evtName, func, false);
                } else if (obj.attachEvent !== undefined && obj.attachEvent !== null) {
                    obj.attachEvent(evtName, func);
                } else {
                    if (this.getAttribute("on" + evtName) !== undefined) {
                        obj["on" + evtName] = func;
                    } else {
                        obj[evtName] = func;
                    }
                }

            }

            function removeEvents(obj, evtName, func) {
                if (obj.removeEventListener !== undefined && obj.removeEventListener !== null) {
                    obj.removeEventListener(evtName, func, false);
                } else if (obj.detachEvent !== undefined && obj.detachEvent !== null) {
                    obj.detachEvent(evtName, func);
                } else {
                    if (this.getAttribute("on" + evtName) !== undefined) {
                        obj["on" + evtName] = null;
                    } else {
                        obj[evtName] = null;
                    }
                }

            }

        </script>