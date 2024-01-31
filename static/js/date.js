document.getElementById('dateInput').addEventListener('change', function() {
    var selectedDate = new Date(this.value);
    var formattedDate = selectedDate.getDate().toString().padStart(2, '0') + '.' + 
                        (selectedDate.getMonth() + 1).toString().padStart(2, '0') + '.' + 
                        selectedDate.getFullYear();

    this.value = formattedDate;
});