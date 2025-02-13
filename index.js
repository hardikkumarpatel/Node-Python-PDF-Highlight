const childProcess = require("node:child_process");

class App {
    static getHighlightPDFContent = (pdfPath, outputPath, highlights) => {
        return new Promise((resolve, reject) => {
            const pythonProcess = childProcess.spawn('python3', ['highlight_pdf.py']);

            const input = JSON.stringify({
                pdf_path: pdfPath,
                output_path: outputPath,
                highlights: highlights,
            });

            let result = "", error = "";

            pythonProcess.stdin.write(input);
            pythonProcess.stdin.end();

            pythonProcess.stdout.on('data', (data) => {
                result += data.toString();
            });

            pythonProcess.stderr.on('data', (data) => {
                error += data.toString();
            });

            pythonProcess.on('close', (code) => {
                if (code === 0) {
                    resolve(JSON.parse(result));
                } else {
                    reject(new Error(`Python script error: ${error}`));
                }
            });
        })
    }
}

const highlights = {
    "0": ["Lorem Ipsum", "Test", "1960s", "desktop"],  
   
};
App.getHighlightPDFContent('input.pdf', 'output.pdf', highlights, [0, 0, 1]).then(console.log).catch(console.error);