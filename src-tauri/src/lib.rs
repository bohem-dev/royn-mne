use std::process::Command;
use tauri::command;

#[command]
fn run_pipeline(pipeline_json: String) -> Result<String, String> {
    let output = Command::new("python")
        .args(["-m", "backend.core", &pipeline_json])
        .output()
        .map_err(|e| e.to_string())?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![run_pipeline])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
