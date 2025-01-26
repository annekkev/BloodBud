<?php
   echo "<b>File to be uploaded: </b>" . $_FILES["filename"]["name"] . "<br>";
   echo "<b>Type: </b>" . $_FILES["filename"]["type"] . "<br>";
   echo "<b>File Size: </b>" . $_FILES["filename"]["size"]/1024 . "<br>";
   echo "<b>Store in: </b>" . $_FILES["filename"]["tmp_name"] . "<br>";

   if (file_exists($_FILES["filename"]["name"])){
      echo "<h3>The file already exists</h3>";
   } else {
      move_uploaded_file($_FILES["filename"]["tmp_name"], $_FILES["filename"]["name"]);
      echo "<h3>File Successfully Uploaded</h3>";
   }
?>