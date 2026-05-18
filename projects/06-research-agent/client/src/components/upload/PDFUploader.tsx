"use client";

import { useState } from "react";

export default function PDFUploader() {
    const [loading, setLoading] =
        useState(false);

    const [message, setMessage] =
        useState("");

    // -----------------------------------
    // Upload PDF
    // -----------------------------------

    const uploadPDF = async (
        file: File
    ) => {
        try {
            setLoading(true);

            setMessage("");

            const formData =
                new FormData();

            formData.append(
                "file",
                file
            );

            const response = await fetch(
                "http://127.0.0.1:8000/upload/",
                {
                    method: "POST",
                    body: formData,
                }
            );

            const data =
                await response.json();

            setMessage(
                data.message
            );
        } catch (error) {
            console.error(error);

            setMessage(
                "Upload failed"
            );
        } finally {
            setLoading(false);
        }
    };

    // -----------------------------------
    // UI
    // -----------------------------------

    return (
        <div
            className="
        bg-zinc-900
        border
        border-zinc-800
        rounded-2xl
        p-6
        mb-6
      "
        >
            <h2 className="text-2xl font-bold mb-4">
                Upload PDF
            </h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => {
                    const file =
                        e.target.files?.[0];

                    if (file) {
                        uploadPDF(file);
                    }
                }}
            />

            {loading && (
                <p className="mt-4 text-zinc-400">
                    Uploading...
                </p>
            )}

            {message && (
                <p className="mt-4 text-green-400">
                    {message}
                </p>
            )}
        </div>
    );
}