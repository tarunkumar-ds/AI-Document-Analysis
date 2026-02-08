async function analyze() {

    const file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Please select a PDF file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    try {
        const response = await fetch("https://ai-document-analysis.onrender.com", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("loading").classList.add("hidden");

        if (data.status !== "success") {
            alert(data.message || "Analysis failed");
            return;
        }

        document.getElementById("summary").innerText = data.summary;

        const keywordsDiv = document.getElementById("keywords");
        keywordsDiv.innerHTML = "";

        data.keywords.forEach(word => {
            const span = document.createElement("span");
            span.innerText = word;
            keywordsDiv.appendChild(span);
        });

        const sentiment = document.getElementById("sentiment");
        sentiment.innerText = data.sentiment;
        sentiment.className = data.sentiment;

        document.getElementById("result").classList.remove("hidden");

    } catch (err) {
        document.getElementById("loading").classList.add("hidden");
        alert("Backend not running");
    }
}

