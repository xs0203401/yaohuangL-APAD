open class Report(val title: String="", 
                  val imageURL: String="", 
                  val description: String=""){
    open fun getReportDetails(): String { 
        return title + ": " + description
    }
}

abstract class ReportDecorator(report: Report): Report(report.title, report.imageURL, report.description) {
    override abstract fun getReportDetails(): String
}

class LocationDecorator(val report: Report, val latitude: Int, val longitude: Int): ReportDecorator(report) {
    override fun getReportDetails(): String {
        return report.getReportDetails() + " - Location: (" + latitude + ", " + longitude + ")"
    }
}

class UrgentDecorator(val report: Report): ReportDecorator(report) {
    override fun getReportDetails(): String {
        return "URGENT: " + report.getReportDetails()
    }
}

fun main(args: Array<String>) {
	val report = Report("test-report-1_title","test-report-1_image", "test-report-1_description")
    println(report.getReportDetails())
    val report_loc = LocationDecorator(report,10,20)
    println(report_loc.getReportDetails())
}
