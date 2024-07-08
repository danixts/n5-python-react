enum FileType {
  JSON = "json",
  CSV = "csv",
}

interface TypeFormatFiles {
  [key: string]: string;
}

const TYPE_FORMAT_FILE: TypeFormatFiles = {
  [FileType.JSON]: "application/json",
  [FileType.CSV]: "text/csv",
};

export const useDownload = () => {
  return (data: string, typeReport: string) => {
    const blob = new Blob([data], { type: TYPE_FORMAT_FILE[typeReport] });
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = `Report.${typeReport}`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };
};
