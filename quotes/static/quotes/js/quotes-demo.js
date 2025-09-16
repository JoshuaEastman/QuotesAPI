(function () {
    const $ = (sel) => document.querySelector(sel);
    const tagEl = $('#tagInput');
    const outEl = $('#output');
    const curlEl = $('#curlBox');
    const fetchBtn = $('#fetchBtn');
    const clearBtn = $('#clearBtn');

    function endpoint(tag) {
        const base = window.QUOTES_RANDOM_URL; // injected by template
        return tag ? `${base}?tag=${encodeURIComponent(tag)}` : base;
    }

    function render(data, status) {
        const code = document.createElement("code");
        code.textContent = JSON.stringify(data, null, 2);
        outEl.innerHTML = "";
        const pre = document.createElement("pre");
        pre.appendChild(code);

        const statusP = document.createElement("p");
        statusP.innerHTML = `<strong>Status:</strong> ${status}`;

        outEl.appendChild(statusP);
        outEl.appendChild(pre);
    }

    function updateCurl(tag) {
        const url = window.location.origin + endpoint(tag);
        curlEl.textContent = `curl -s ${url}`;
    }

    fetchBtn?.addEventListener("click", async () => {
        const tag = tagEl?.value.trim();
        updateCurl(tag);
        try {
            const res = await fetch(endpoint(tag));
            const data = await res.json();
            render(data, res.status);
        } catch (e) {
            render ({ error: String(e) }, "error");
        }
    });

    clearBtn?.addEventListener("click", () => {
        if (tagEl) tagEl.value = "";
        if (outEl) outEl.innerHTML = "";
        if (curlEl) curlEl.textContent = "";
    });

    // Initialize cURL with empty tag
    updateCurl("");
})();